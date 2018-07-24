#!/bin/bash

service_file_path=/lib/systemd/system/icum.service
cat << 'EOF' > ${service_file_path}
[Unit]
Description=ICUMister Service
After=multi-user.target

[Service]
User=pi
ExecStart=/bin/bash /home/pi/ICUMister/start.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOF

chmod 644 ${service_file_path}
systemctl daemon-reload
systemctl enable icum.service
service icum restart
