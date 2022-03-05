function Estimation=Outlier_Check(a1,a2,a3,a4)
if imag(a1)~=0
    var0=var([a2,a3,a4]);
    var1=var([a2,a3]);
    var2=var([a3,a4]);
    var3=var([a2,a4]);
    Minimum=min([var0,var1,var2,var3]);
    if var0<10
        Estimation=(a2+a3+a4)/3;
    else
        if Minimum==var0
             Estimation=(a2+a3+a4)/3;
        elseif Minimum==var1
             Estimation=(a2+a3)/2;
        elseif Minimum==var2
             Estimation=(a3+a4)/2;
        else
             Estimation=(a2+a4)/2;
        end
    end
    State=1;
elseif imag(a2)~=0
    var0=var([a1,a3,a4]);
    var1=var([a1,a3]);
    var2=var([a3,a4]);
    var3=var([a1,a4]);
    Minimum=min([var0,var1,var2,var3]);
    if var0<10
        Estimation=(a1+a3+a4)/3;
    else
        if Minimum==var0
             Estimation=(a1+a3+a4)/3;
        elseif Minimum==var1
             Estimation=(a1+a3)/2;
        elseif Minimum==var2
             Estimation=(a3+a4)/2;
        else
             Estimation=(a1+a4)/2;
        end
    end
    State=1;
elseif imag(a3)~=0
    var0=var([a2,a1,a4]);
    var1=var([a2,a1]);
    var2=var([a1,a4]);
    var3=var([a2,a4]);
    Minimum=min([var0,var1,var2,var3]);
    if var0<10
        Estimation=(a2+a1+a4)/3;
    else
        if Minimum==var0
             Estimation=(a2+a1+a4)/3;
        elseif Minimum==var1
             Estimation=(a2+a1)/2;
        elseif Minimum==var2
             Estimation=(a1+a4)/2;
        else
             Estimation=(a2+a4)/2;
        end
    end
    State=1;
elseif imag(a4)~=0
    var0=var([a2,a3,a1]);
    var1=var([a2,a3]);
    var2=var([a3,a1]);
    var3=var([a2,a1]);
    Minimum=min([var0,var1,var2,var3]);
    if var0<10
        Estimation=(a2+a3+a1)/3;
    else
        if Minimum==var0
             Estimation=(a2+a3+a1)/3;
        elseif Minimum==var1
             Estimation=(a2+a3)/2;
        elseif Minimum==var2
             Estimation=(a3+a1)/2;
        else
             Estimation=(a2+a1)/2;
        end
    end
    State=1;
else
    State=0;
end
if State==0
    var0=var([a1,a2,a3,a4]);
    var1=var([a1,a2,a3]);
    var2=var([a1,a2,a4]);
    var3=var([a1,a4,a3]);
    var4=var([a4,a2,a3]);
    Minimum=min([var0,var1,var2,var3,var4]);
    if var0<30
        Estimation=(a1+a2+a3+a4)/4;
    else
        if Minimum==var0
             Estimation=(a1+a2+a3+a4)/4;
        elseif Minimum==var1
             Estimation=(a1+a2+a3)/3;
        elseif Minimum==var2
             Estimation=(a1+a2+a4)/3;
        elseif Minimum==var3
             Estimation=(a1+a4+a3)/3;
        else
             Estimation=(a4+a2+a3)/3;
        end
    end
end
Estimation=real(Estimation);
end