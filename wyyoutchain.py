pre = "<iframe frameborder=\"no\" border=\"0\" marginwidth=\"0\" marginheight=\"0\" width="330" height="86" src=\"//music.163.com/outchain/player?type=2&id="
suf = "&auto=0&height=66\"></iframe>"
musicid = input('Input the share link:\n>>> ').split('&')[0].split('id=')[1]
print(pre+musicid+suf)
