# Use this script to run the simulation multiple times (when analysing results).
for (( c = 0; c <= 5; c++ ))
do
	python main.py 150000 5 10000 0.01 2 >> results.csv
done