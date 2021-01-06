close all
clear
clc
str = 'F:\lobe\lobe_data_before\test_masks_15\';
files = dir(strcat(str,'*.nii'));
for i=1:3
    nii = load_nii([str,files(i).name]);
    img = nii.img;  % ��Ϊ����ļ���img��head�������֣�����img������ͼ������
    img_temp = img;
    if(ismember(6,img))
        img(img_temp==3)=1;
        img(img_temp==4)=2;
        img(img_temp==1)=3;
        img(img_temp==6)=4;
        img(img_temp==2)=5;
    end
    nii.img = img;
    save_nii(nii, ['F:\lobe\lobe_data_before\test_masks_15_12345\', files(i).name, '.gz'])
end
