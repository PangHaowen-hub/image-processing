%% nii resize 效果不好
close all
clear
clc
str = 'F:\lobe\lobe_data_all_before\test_masks_15_12345\';
files = dir(strcat(str,'*.gz'));
for i=1:1
    nii = load_nii([str,files(i).name]);
    img = nii.img;  % 因为这个文件有img和head二个部分，其中img部分是图像数据
    img_temp = img;
    img_size = size(img_temp);
    img_resize = zeros(320,320,img_size(3));
    for j=1:img_size(3)
       
        temp = imresize(img_temp(:,:,j),[320 320]);
        img_resize(:,:,j) = temp;
    end 
    niiresize.hdr = nii.hdr;
    niiresize.filetype = nii.filetype;
    niiresize.fileprefix = 'F:\lobe\lobe_data_before\test_masks_15_12345\test';
    niiresize.machine = nii.machine;
    niiresize.hdr.dime.dim = [3,320,320,287,1,1,1,1];
    niiresize.img = uint16(img_resize);
    niiresize.original = nii.original;
    save_nii(niiresize, 'test.nii')
%   save_nii(nii, ['F:\lobe\lobe_data_before\test_masks_15_12345\', files(i).name, '.gz'])
end
