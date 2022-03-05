Estimation_matrix=zeros(1,36);
Real_matrix=zeros(1,36);
count=1;
Angle_difference=0;
for rx=-5:2:5
    for ry=-5:2:5
        [Estimation,Real]=Estimation_simulation(rx,ry);
        Angle_difference=Angle_difference+abs(Estimation-Real);
        Estimation_matrix(count)=Estimation;
        disp(count)
        Real_matrix(count)=Real;
        count=count+1;
    end
end
Average_error=Angle_difference/36
        