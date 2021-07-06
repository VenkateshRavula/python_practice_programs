def write_multiple_lines(file, seperator, *args):
  f = open(file, 'w')
  f.write(seperator.join(args))

write_multiple_lines('write_sample.txt', '-', "hai", "hello")
