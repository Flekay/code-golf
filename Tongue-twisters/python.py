s='''How much^ would a^* *,
If a^* could *^?
A^* would * all the^ he could *
If a^* would *^.

%#ed a peck of#led&.
A peck of#led& %#ed.
If %#ed a peck of#led&,
Where's the peck of#led& %#ed?

She s! @! by the @ore,
The sh! she s! are @!, I'm sure.
So if she s! @! on the @ore,
Then I'm sure she s! @ore sh!.'''
for c in zip('^*#&%!@',' wood,chuck, pick, peppers,Peter Piper,ells,seash'.split(',')):s=s.replace(*c)
print(s)
