close all
clear
clc
str = 'F:\my_lobe_data\after\LU\masks\';
files = dir(strcat(str,'*.nii.gz'));
for i=1:length(files)
    nii = load_nii([str,files(i).name]);
    img = nii.img;  % 因为这个文件有img和head二个部分，其中img部分是图像数据
    img_temp = img;
%     if(ismember(6,img))
    img(img_temp==3)=1;
    img(img_temp==4)=2;
    img(img_temp==1)=3;
    img(img_temp==6)=4;
    img(img_temp==2)=5;

%     end
    nii.img = img;
    save_nii(nii, ['F:\my_lobe_data\after\LU\masks\', files(i).name])

end
