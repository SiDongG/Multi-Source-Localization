function Estimation=Outlier_Check(a1,a2,a3,a4)
average=(a1+a2+a3+a4)/4;
if imag(a1)~=0
    Estimation=(a2+a3+a4)/3;
    State=1;
elseif imag(a2)~=0
    Estimation=(a1+a3+a4)/3;
    State=1;
elseif imag(a3)~=0
    Estimation=(a2+a1+a4)/3;
    State=1;
elseif imag(a4)~=0
    Estimation=(a2+a3+a1)/3;
    State=1;
else
    State=0;
end
if State==0 && abs(a1-average)>10
    Estimation=(a2+a3+a4)/3;
elseif State==0 && abs(a2-average)>10
    Estimation=(a1+a3+a4)/3;
elseif State==0 && abs(a3-average)>10
    Estimation=(a2+a1+a4)/3;
elseif State==0 && abs(a4-average)>10
    Estimation=(a2+a3+a1)/3;
elseif State==0
    Estimation=(a1+a2+a3+a4)/4;
end
end