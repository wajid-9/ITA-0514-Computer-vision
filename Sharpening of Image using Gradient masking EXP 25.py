a = imread(r"C:\Users\shaik\OneDrive\Pictures\Picture3.png");
Lap = [0, 1, 0; 1, -4, 1; 0, 1, 0];
a1 = conv2(double(a), Lap, 'same');
a2 = uint8(a1);
figure;
subplot(1, 2, 1), imshow(a), title('Original Image');
subplot(1, 2, 2), imshow(abs(a - a2), []), title('Absolute Difference');
lap = [-1, -1, -1; -1, 8, -1; -1, -1, -1];
a3 = conv2(double(a), lap, 'same');
a4 = uint8(a3);
figure;
subplot(1, 2, 1), imshow(a), title('Original Image');
subplot(1, 2, 2), imshow(abs(a + a4), []), title('Sum of Original and Laplacian');
imwrite(abs(a - a2), 'absolute_difference.png');
imwrite(abs(a + a4), 'sum_of_original_and_laplacian.png');
