def render_input(field):
  return f'<input id="id_{field}" name="{field}">'

username = render_input('username')

def dec(user, tag):
  return f'<{tag}>{user}</{tag}>'

print(dec(username, "p"))