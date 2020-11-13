cd uploads
rm -rf work
mkdir work
ls
cp temp.zip work
cd work
unzip temp.zip
/home/leuat/code/nutil/Debug/Nutil nutil.nut 4
#open /Users/leuat/code/nutil/Debug/Nutil.app nutil.nut 4
zip -r results.zip 4_output_dir
mv results.zip ../../results/results_$1.zip
cd ..
cd ..

