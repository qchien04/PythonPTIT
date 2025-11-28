import stun

nat_type, external_ip, external_port = stun.get_ip_info()
print(f"NAT Type: {nat_type}")
print(f"Public IP: {external_ip}:{external_port}")