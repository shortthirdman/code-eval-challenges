digits=( -**----*--***--***---*---****--**--****--**---**--
         *--*--**-----*----*-*--*-*----*-------*-*--*-*--*-
         *--*---*---**---**--****-***--***----*---**---***-
         *--*---*--*-------*----*----*-*--*--*---*--*----*-
         -**---***-****-***-----*-***---**---*----**---**--
         -------------------------------------------------- )
w=5
h=6
tr -cd "[:digit:]\n" <$1 | while read line || [ -n "$line" ]; do
  for ((i=0; i<$h; i++)); do
    for ((j=0; j<${#line}; j++)); do
      printf "%s" "${digits[$i]:$(( ${line:$j:1}*$w )):$w}"
    done
    echo
  done
done
