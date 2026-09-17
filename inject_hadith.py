with open('hadith_data.txt') as f:
    data = f.read()
with open('hadith_js.txt') as f:
    js = f.read()
with open('templates/hadith.html') as f:
    content = f.read()

old = '<script>\n/* PART 2 WILL BE INJECTED */\n</script>'
new = '<script>\n' + data + '\n\n' + js + '\n</script>'

if old in content:
    content = content.replace(old, new)
    print('Injected OK')
else:
    print('Placeholder not found!')

with open('templates/hadith.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Total size:', len(content))
