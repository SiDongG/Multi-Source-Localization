Estimation_matrix=zeros(1,36);
Real_matrix=zeros(1,36);
Estimation2_matrix=zeros(1,36);
Real2_matrix=zeros(1,36);
count=1;
Angle_difference=0;
Distance_difference=0;
for rx=-5:2:5
    for ry=-5:2:5
        [Estimation,Real,Estimation2,Real2]=Estimation_simulation(rx,ry);
        Angle_difference=Angle_difference+abs(Estimation-Real);
        Distance_difference=Distance_difference+abs(Estimation2-Real2);
        Estimation_matrix(count)=Estimation;
        Estimation2_matrix(count)=Estimation2;
        disp(count)
        Real_matrix(count)=Real;
        count=count+1;
    end
end
Average_error=Angle_difference/36
Average_error_distance=Distance_difference/36

Cor_x=zeros(1,36);
Cor_y=zeros(1,36);
Cor_x_real=[-5*ones(1,6),-3*ones(1,6),-1*ones(1,6),1*ones(1,6),3*ones(1,6),5*ones(1,6)];
Cor_y_real=[-5:2:5,-5:2:5,-5:2:5,-5:2:5,-5:2:5,-5:2:5];

for i=1:36
    Cor_x(i)=Estimation2_matrix(i)*cosd(Estimation_matrix(i));
    Cor_y(i)=Estimation2_matrix(i)*sind(Estimation_matrix(i));
end

plot=figure();
scatter(Cor_x,Cor_y);
hold on
scatter(Cor_x_real,Cor_y_real);
xlabel('x coordinate in meter');
ylabel('y coordinate in meter');
legend('Estimated_position','Real_position');
