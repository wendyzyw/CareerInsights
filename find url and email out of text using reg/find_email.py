pat_email = re.compile(r'''
(?xm) # verbose identify URLs in text (and multiline)
(?=^.{11} # Mail header matcher
(?<!Message-ID:| # rule out Message-ID's as best possible
In-Reply-To)) # ...and also In-Reply-To
(.*?)( # must grab to email to allow prior lookbehind
([A-Za-z0-9-]+\.)? # maybe an initial part: DAVID.mertz@gnosis.cx
[A-Za-z0-9-]+ # definitely some local user: MERTZ@gnosis.cx
@ # ...needs an at sign in the middle
(\w+\.?){2,} # at least two domain groups, e.g. (gnosis.)((?=[\s\.,>)'"\]]) # assert: followed by white or clause ending
) # end of match group
''')