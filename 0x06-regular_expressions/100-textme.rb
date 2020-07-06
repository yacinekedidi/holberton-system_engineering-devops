#!/usr/bin/env ruby
# a = ARGV[0].scan(/(?<=from:)[^\]]+/).join
a = ARGV[0].scan(/(?<=from:)[\w+.-]+/).join
# a = ARGV[0].scan(/(?<=to:)[^\]]+/).join
b = ARGV[0].scan(/(?<=to:)[\w+.-]+/).join
# a = ARGV[0].scan(/(?<=flags:)[^\]]+/).join
c =  ARGV[0].scan(/(?<=flags:)[\w:+.-]+/).join
puts a + "," + b + "," + c
