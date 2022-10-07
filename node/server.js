const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

var osutils = require('os-utils');

var ut_sec = osutils.sysUptime();
var ut_min = ut_sec/60;
var ut_hour = ut_min/60;

ut_sec = Math.floor(ut_sec);
ut_min = Math.floor(ut_min);
ut_hour = Math.floor(ut_hour);

ut_hour = ut_hour%60;
ut_min = ut_min%60;
ut_sec = ut_sec%60;




http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${ut_hour + " Hour(s) " + ut_min + " minute(s) " + ut_sec + " second(s)"} </p>
        <p>Total Memory: ${osutils.totalmem()} MB</p>
        <p>Free Memory: ${osutils.freemem()} MB</p>
        <p>Number of CPUs: ${osutils.cpuCount()} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");


//https://tutorialedge.net/nodejs/monitoring-server-stats-with-nodejs/