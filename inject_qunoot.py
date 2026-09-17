with open('qunoot_js.txt') as f:
    js = f.read()
with open('templates/qunoot.html') as f:
    c = f.read()
old = '<!-- JS_HERE -->'
if old not in c:
    old2 = '</body>'
    c = c.replace('</body>', '<script>\n' + js + '\n</script>\n</body>')
    print('Injected before body')
else:
    c = c.replace(old, '<script>\n' + js + '\n</script>')
    print('Injected at marker')
with open('templates/qunoot.html', 'w') as f:
    f.write(c)
print('Total:', len(c), 'bytes')
