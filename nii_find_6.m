close all
clear
clc
str = 'F:\lobe\lobe_data_before\train_masks_75_12345\';
files = dir(strcat(str,'*.nii.gz'));
for i=1:75
    nii = load_nii([str,files(i).name]);
    img = nii.img;  % ��Ϊ����ļ���img��head�������֣�����img������ͼ������
    ismember(6,img);
    max(max(max(img)))
    img(img~=0 & img~=1 & img~=2 & img~=3 & img~=4 &img~=5);
end
