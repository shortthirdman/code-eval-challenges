use strict;
open( INFILE, "<", $ARGV[0] )
  or die("Cannot open file $ARGV[0] for reading: $!");
while ( my $line = <INFILE> ) {
    next if ( $line =~ m/^\s$/ );
    chomp($line);
    my @r = map {
        if ( $_ =~ /^[[:upper:]]/ )
        {
            lc $_;
        }
        else {
            uc $_;
        }
    } split( //, $line );
    printf( "%s\n", join( '', @r ) );
}
close(INFILE);
