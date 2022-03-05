function real=angle(rx,ry)
if rx>=0
    real=atand(ry/rx);
elseif rx<=0 && ry<=0
    real=atand(ry/rx)-180;
else
    real=atand(ry/rx)+180;
end