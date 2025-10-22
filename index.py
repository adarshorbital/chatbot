cd /web/groups/gustyai/public_html
cat > test_cgi.py << 'EOF'
#!/usr/bin/env python3
print("Content-Type: text/html\n")
print("<h1>CGI is working!</h1>")
EOF

chmod 755 test_cgi.py