#!/bin/bash

SCRIPT=`basename "$0"`
DIR=$1

if [ -z "$1" ]
	then
		echo "Please use './$SCRIPT <directory>' to download the Mnist data files"
		exit 1
fi		
	

mkdir -p $DIR
if [ $? -ne 0 ] ; 
	then
		echo "Failed to create directory. Do you have permissions to create this directory?"
		exit 1
fi

if ! [ -e $DIR/mnist/train-images-idx3-ubyte.gz ]
	then
		wget -P $DIR/mnist/ http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
fi
gzip -d $DIR/mnist/train-images-idx3-ubyte.gz

if ! [ -e $DIR/mnist/train-labels-idx1-ubyte.gz ]
	then
		wget -P $DIR/mnist/ http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
fi
gzip -d $DIR/mnist/train-labels-idx1-ubyte.gz

if ! [ -e $DIR/mnist/t10k-images-idx3-ubyte.gz ]
	then
		wget -P $DIR/mnist/ http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
fi
gzip -d $DIR/mnist/t10k-images-idx3-ubyte.gz

if ! [ -e $DIR/mnist/t10k-labels-idx1-ubyte.gz ]
	then
		wget -P $DIR/mnist/ http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
fi
gzip -d $DIR/mnist/t10k-labels-idx1-ubyte.gz
