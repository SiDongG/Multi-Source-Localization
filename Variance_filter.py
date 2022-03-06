def Outlier(a1,a2,a3,a4):
    if a1==360:
        var0=variance((a2,a3,a4))
        var1=variance((a2,a3))
        var2=variance((a2,a4))
        var3=variance((a3,a4))
        Minimum=min(var0,var1,var2,var3)
        if var0<10:
            Estimation=(a2+a3+a4)/3
        else:
            if Minimum==var0:
                Estimation=(a2+a3+a4)/3
            elif Minimum==var1:
                Estimation=(a2+a3)/2
            elif Minimum==var2:
                Estimation=(a2+a4)/2
            else:
                Estimation=(a3+a4)/2
        State=1
    elif a2==360:
         var0=variance((a1,a3,a4))
         var1=variance((a1,a3))
         var2=variance((a1,a4))
         var3=variance((a3,a4))
         Minimum=min(var0,var1,var2,var3)
         if var0<10:
             Estimation=(a1+a3+a4)/3
         else:
             if Minimum==var0:
                 Estimation=(a1+a3+a4)/3
             elif Minimum==var1:
                 Estimation=(a1+a3)/2
             elif Minimum==var2:
                 Estimation=(a1+a4)/2
             else:
                 Estimation=(a3+a4)/2
         State=1
    elif a3==360:
           var0=variance((a1,a2,a4))
           var1=variance((a1,a2))
           var2=variance((a1,a4))
           var3=variance((a2,a4))
           Minimum=min(var0,var1,var2,var3)
           if var0<10:
                Estimation=(a1+a2+a4)/3
           else:
                if Minimum==var0:
                     Estimation=(a1+a2+a4)/3
                elif Minimum==var1:
                     Estimation=(a1+a2)/2
                elif Minimum==var2:
                     Estimation=(a1+a4)/2
                else:
                     Estimation=(a2+a4)/2
           State=1
    elif a4==360:
            var0=variance((a1,a2,a3))
            var1=variance((a1,a2))
            var2=variance((a1,a3))
            var3=variance((a2,a3))
            Minimum=min(var0,var1,var2,var3)
            if var0<10:
                Estimation=(a1+a2+a3)/3
            else:
                if Minimum==var0:
                    Estimation=(a1+a2+a3)/3
                elif Minimum==var1:
                    Estimation=(a1+a2)/2
                elif Minimum==var2:
                    Estimation=(a1+a3)/2
                else:
                    Estimation=(a2+a3)/2
            State=1
    else:
        State=0

    if State==0:
        var0=variance((a1,a2,a3,a4))
        var1=variance((a1,a2,a3))
        var2=variance((a1,a2,a4))
        var3=variance((a1,a3,a4))
        var4=variance((a2,a3,a4))
        Min=min(var0,var1,var2,var3,var4)
        if var0<20:
            Estimation=mean((a1,a2,a3,a4))
        else:
            if Min==var1:
                Estimation=(a1+a2+a3)/3
            elif Min==var2:
                Estimation=(a1+a2+a4)/3
            elif Min==var3:
                Estimation=(a1+a3+a4)/3
            elif Min==var4:
                Estimation=(a2+a3+a4)/3
            else:
                Estimation=(a1+a2+a3+a4)/4
    return Estimation 
        
         
