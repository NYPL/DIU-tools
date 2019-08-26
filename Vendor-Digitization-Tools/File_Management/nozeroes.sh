shopt -s extglob
for i in 0*[^0]
do mv "$i" "${i##*(0)}"
done
