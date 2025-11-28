def kt(input_file, output_file):
    contacts = []
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                name = ' '.join(parts[:-1])
                phone = parts[-1]
                contacts.append((name, phone))
        contacts.sort(key=lambda x: x[0].split() + [x[1]])

    with open(output_file, 'w', encoding='utf-8') as file:
        for name, phone in contacts:
            file.write(f"{name} {phone}\n")
kt('SOTAY.txt', 'DIENTHOAI.txt')
