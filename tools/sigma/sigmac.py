title: Detect XSS Attempts by keywords
id: 553a450b8-604d-41a9-8587-a28334aaddfb
status: experimental
description: Detects XSS that use GET requests by keyword searches in URL strings
author: Saw Win Naung
date: 2020/02/22
logsource:
  category: webserver
detection:
  keywords:
    - =cookie
    - =script
    - =onload
    - =onmouseover
  condition: keywords
fields:
  - client_ip
  - vhost
  - url
  - response
falsepositives:
  - Java scripts,CSS Files and PNG files
  - User searches in search boxes of the respective website
level: high
