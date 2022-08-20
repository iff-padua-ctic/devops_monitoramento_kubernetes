#Github do Projeto: https://github.com/prometheus/client_python/blob/master/README.md
#https://linuxhint.com/monitor-python-applications-prometheus/
#https://geekyhumans.com/monitor-python-scripts-using-prometheus/
#https://trstringer.com/quick-and-easy-prometheus-exporter/
#https://gist.github.com/rchakode/8c362c23876b82c85e997c029b076540
#https://www.gspann.com/resources/blogs/developing-custom-exporter-for-prometheus-using-python/
#https://python.tutorialink.com/get-cpu-memory-disk-data-using-python-script-from-node-exporter-metrics/


import http.server
import prometheus_client as prom
import time
import psutil
import socket


#host = socket.gethostname()

SYSTEM_USAGE = prom.Gauge('system_usage','Hold current system resource usage', ['resource_type'])


class ServerHandler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.end_headers()
    self.wfile.write(b"Hello World!")




if __name__ == "__main__":
    prom.start_http_server(8000)
    #server = http.server.HTTPServer(('', 8001), ServerHandler)
    print("Prometheus metrics available on port 8000 /metrics")
    print("HTTP server available on port 8001")
    #server.serve_forever()



while(True):
    time.sleep(5)
    SYSTEM_USAGE.labels('cpu_usage_percent').set(psutil.cpu_percent())
    SYSTEM_USAGE.labels('memory_usage_bytes').set(psutil.virtual_memory()[2])

