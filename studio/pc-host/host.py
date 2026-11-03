#!/usr/bin/env python3
"""Private ASO Studio host; expose only through Tailscale Serve."""
import base64,hmac,json,mimetypes,os,re,secrets
from datetime import datetime,timezone
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote,urlparse
ROOT=Path(__file__).resolve().parents[2]; STUDIO=ROOT/"studio"
DATA=Path(os.environ.get("ASO_DATA_DIR",str(Path.home()/"ASO-Studio-Data"))).resolve()
INBOX=DATA/"inbox"; INBOX.mkdir(parents=True,exist_ok=True)
LIMIT=int(os.environ.get("ASO_MAX_UPLOAD_MB","2048"))*1024*1024
PORT=int(os.environ.get("ASO_PORT","8765")); USER=os.environ.get("ASO_USER","aso"); PASSWORD=os.environ.get("ASO_PASSWORD","")
if len(PASSWORD)<20: raise SystemExit("ASO_PASSWORD must be 20+ characters; run setup-windows.ps1.")
class H(BaseHTTPRequestHandler):
 server_version="ASOStudioHost/1.0"
 def authorized(self):
  try:
   scheme,token=self.headers.get("Authorization","").split(" ",1); u,p=base64.b64decode(token).decode().split(":",1)
  except Exception: scheme=u=p=""
  ok=scheme.lower()=="basic" and hmac.compare_digest(u,USER) and hmac.compare_digest(p,PASSWORD)
  if not ok: self.send_response(401); self.send_header("WWW-Authenticate",'Basic realm="ASO Studio", charset="UTF-8"'); self.end_headers()
  return ok
 def reply(self,code,data,ctype="application/json; charset=utf-8"):
  self.send_response(code); self.send_header("Content-Type",ctype); self.send_header("X-Content-Type-Options","nosniff"); self.send_header("Cache-Control","no-store"); self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data)
 def do_GET(self):
  if not self.authorized(): return
  path=urlparse(self.path).path
  if path=="/api/status":
   ups=[{"name":p.name,"bytes":p.stat().st_size,"modified":datetime.fromtimestamp(p.stat().st_mtime,timezone.utc).isoformat()} for p in sorted(INBOX.iterdir(),key=lambda x:x.stat().st_mtime,reverse=True) if p.is_file()][:50]
   return self.reply(200,json.dumps({"ok":True,"host":os.environ.get("COMPUTERNAME","production-pc"),"inbox":str(INBOX),"uploads":ups,"max_upload_bytes":LIMIT,"rendering":"not connected yet"}).encode())
  if path=="/": path="/pc.html"
  f=(STUDIO/unquote(path.lstrip("/"))).resolve()
  if STUDIO not in f.parents or not f.is_file(): return self.reply(404,b'{"error":"not found"}')
  return self.reply(200,f.read_bytes(),mimetypes.guess_type(f.name)[0] or "application/octet-stream")
 def do_POST(self):
  if not self.authorized(): return
  if urlparse(self.path).path!="/api/upload": return self.reply(404,b'{"error":"not found"}')
  try: n=int(self.headers.get("Content-Length","0"))
  except ValueError: n=0
  if n<1 or n>LIMIT: return self.reply(413,b'{"error":"empty upload or size limit exceeded"}')
  name=re.sub(r"[^A-Za-z0-9._-]","_",Path(unquote(self.headers.get("X-File-Name","handoff.zip"))).name)[:120]
  if not name.lower().endswith((".zip",".json",".wav",".mp4",".mov",".png",".jpg",".jpeg",".webp")): return self.reply(415,b'{"error":"file type not allowed"}')
  tmp=INBOX/(secrets.token_hex(8)+".uploading"); dst=INBOX/(secrets.token_hex(8)+"-"+name)
  try:
   left=n
   with tmp.open("xb") as out:
    while left:
     chunk=self.rfile.read(min(1048576,left))
     if not chunk: raise ConnectionError("incomplete")
     out.write(chunk); left-=len(chunk)
   tmp.replace(dst)
  except Exception:
   tmp.unlink(missing_ok=True); return self.reply(400,b'{"error":"upload failed; partial file discarded"}')
  return self.reply(201,json.dumps({"ok":True,"saved_as":dst.name,"bytes":n,"next_step":"Received only; import and rendering are not automated yet."}).encode())
 def log_message(self,fmt,*args): print("%s - %s"%(self.client_address[0],fmt%args))
if __name__=="__main__":
 print("ASO host on 127.0.0.1:%s; expose only through Tailscale Serve."%PORT); print("Inbox:",INBOX)
 ThreadingHTTPServer(("127.0.0.1",PORT),H).serve_forever()
