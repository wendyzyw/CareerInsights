import re, fileinput

pat_url = re.compile( r'''
(?x)( # verbose identify URLs within text
(http|ftp|gopher) # make sure we find a resource type
:// # ...needs to be followed by colon-slash-slash
(\w+[:.]?){2,} # at least two domain groups, e.g. (gnosis.)((/?| # could be just the domain name (maybe w/ slash)
[^ \n\r"]+ # or stuff then space, newline, tab, quote
[\w/]) # resource name ends in alphanumeric or slash
(?=[\s\.,>)'"\]]) # assert: followed by white or clause ending
) # end