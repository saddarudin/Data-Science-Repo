# The Hough Transform is a populat technique to detect any shape, if you can represent that shape in a mathematical form.
# The most popular use of the Hough Transform is to detect lines in an image, but it can also be used to detect circles or other shapes.
# It can detect the shape even if it is broken or distorted a little bit.

# Hough Transformation Algorithm
# 1. Edge Detection. For example, using the Canny edge detector.
# 2. Mapping of edge points to the Hough space and storage in an accumulator.
# 3. Interpretation of the accumulator to yield lins of infinite length. 
#    The interpretation is done by thresholding and possibly other constraints.
# 4. Conversion of infinite lines to finite lines.


# Open CV implements two kinds of Hough Line Transforms:
# 1. The Standard Hough Transform (HoughLines method)
# 2. The Probabilistic Hough Line Transform (HoughLinesP method)