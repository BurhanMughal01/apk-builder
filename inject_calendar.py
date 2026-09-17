with open('calendar_js.txt') as f:
    js = f.read()
with open('templates/calendar.html') as f:
    content = f.read()

old = '''<script>
/* PART 2 WILL BE INJECTED */
</script>'''

new = '<script>\n' + js + '\n</script>'

if old in content:
    content = content.replace(old, new)
    print('Injected OK')
else:
    print('Placeholder not found!')

with open('templates/calendar.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Total size:', len(content), 'bytes')
