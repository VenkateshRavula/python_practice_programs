#! /bin/sh

# cycleload.sh
# Krishna --- a primitive script to generate IO load on a server
# the 'conv=fsync' option is to flush data to disk before next op
# the intent of 10M is to have a significant amount of data to be pushed to disk in each count
#  ---- could be 1M also. Keeping a total of 100M at any point
#
# Run as "nohup ./cycleload.sh &"

count=0
end=3000000
#end=4

echo  $(date)  "IO load for bs=1M count =10 flush to disk" > /tmp/cycleload.log
echo  " "  >> /tmp/cycleload.log

while [ $count -lt $end ];
do
  err1=$(dd if=/dev/zero of=/tmp/krsout bs=1M count=100 conv=fsync 2>&1)
  err2=$(dd if=/dev/zero of=/scratch/krsout bs=1M count=100 conv=fsync 2>&1)
#  ./krs.py > x.out
   echo "not used" > x.out
  err3=$(tail -1 x.out)
  echo Iteration $count " " $err2 "&"  $err3 " " $(date) >> /tmp/cycleload.log
  echo Iteration $count " " $err1 " " $(date) >> /tmp/cycleloadlocal.log

  count=$((count + 1))
done

echo " " >> /tmp/cycleload.log
echo "That's all folks!" >> /tmp/cycleload.log

