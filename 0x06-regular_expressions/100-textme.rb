#!/usr/bin/env ruby

# parse log line - format: [SENDER],[RECEIVER],[FLAGS]
# regex for TextMe(app) messages transactions stats
puts ARGV[0].scan(/\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/).join(',')
