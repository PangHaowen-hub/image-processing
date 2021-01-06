close all
clear
clc
str = 'F:\lobe\lobe_data_all_before\train_images_75\';
files = dir(strcat(str,'*.nii.gz'));
for i=1:75
    nii = load_nii([str,files(i).name]);
    size0 = size(nii.img);
    if (size0(1) == 320)
        i
        size0
    end
    
end
