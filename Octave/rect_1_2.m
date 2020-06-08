
function rect_1_2()

    graphics_toolkit('gnuplot');

    mkdir('rect_1.2');

    graph_n('rect_1.2/figure_n_2',   2);
    graph_n('rect_1.2/figure_n_5',   5);
    graph_n('rect_1.2/figure_n_10',   10);
    graph_n('rect_1.2/figure_n_20',   20);

endfunction

function v = volt(x,y,a,b,n, const)

    v=const*cosh(n*pi*x/b)*sin(n*pi*y/b);

endfunction

function e = e_field(x,y,a,b,n, const)

    ex = sinh(n*pi*x/b)*sin(n*pi*y/b);

    ey = cosh(n*pi*x/b)*cos(n*pi*y/b);

    e=const*(n*pi/b)*sqrt(ex^2+ey^2);

endfunction

function s = charge(y,a,b,n, const)

    s = const*(n*pi/b)*sinh(n*pi*a/b)*sin(n*pi*y/b);

endfunction

function graph_v(name, n, a, b, const)

    V(a+1,b+1)=0;

    for ix=1:a*2+1
        for iy=1:b+1
            V(ix,iy)=volt(ix-a,iy,a,b,n, const);
        end
    end

    x=-a:1:a;
    y=0:1:b;

    clf();
    % ugly fix because axis sizes are somehow flipped
    [X,Y] = meshgrid(y,x);

    surf(Y,X,V)
    shading('interp')

    xlabel('x'); ylabel('y'); zlabel('Potencial (V)');

    text=sprintf('Potencial para n=%i',n);
    title(text);

    axis('tight');

    file_name = sprintf('%s_v', name);
    print('-dpng',file_name);

endfunction

function graph_e(name, n, a, b, const)

    E(a+1,b+1)=0;

    for ix=1:a*2+1
        for iy=1:b+1
            E(ix,iy)=e_field(ix-a,iy,a,b,n, const);
        end
    end

    x=-a:1:a;
    y=0:1:b;

    clf();
    % ugly fix because axis sizes are somehow flipped
    [X,Y] = meshgrid(y,x);

    surf(Y,X,E)
    shading('interp')

    xlabel('x'); ylabel('y'); zlabel('Campo Electrico (V/m)');

    text=sprintf('Campo Electrico para n=%i',n);
    title(text);

    axis('tight');

    file_name = sprintf('%s_e', name);
    print('-dpng',file_name);

endfunction


function graph_s1(name, n, a, b, const)

    S(b+1)=0;


    for iy=1:b+1
        S(iy)=charge(iy,a,b,n, const);
    end

    clf();

    plot(S)

    ylabel('Densidad de carga (C/m\^2)')
    xlabel('y');

    text=sprintf('Densidad de carga en la pared x=a para n=%i',n);
    title(text);

    axis('tight');

    file_name = sprintf('%s_s1', name);
    print('-dpng',file_name);

endfunction

function graph_s2(name, n, a, b, const)

    S(b+1)=0;


    for iy=1:b+1
        S(iy)=charge(iy,a,b,n, const);
    end

    clf();

    plot(S)

    ylabel('Densidad de carga (C/m\^2)')
    xlabel('y');

    text=sprintf('Densidad de carga en la pared x=-a para n=%i',n);
    title(text);

    axis('tight');

    file_name = sprintf('%s_s2', name);
    print('-dpng',file_name);

endfunction

function graph_n(name, n)
    a=200;
    b=100;

    % pre calculating magic constant ;)

    const=(12*b^4/(n*pi)^3-2*b^4/(n*pi))*cos(n*pi) + (6*b^4/(n*pi)^2-12*b^4/(n*pi)^4)*sin(n*pi) - (5*b/(n*pi))*(cos(n*pi)-1);

    const=4*const/(b*cosh(n*pi*a/b));

    graph_v(name,   n, a, b, const);
    graph_e(name,   n, a, b, const);
    graph_s1(name,   n, a, b, const);
    graph_s2(name,   n, -a, b, const);

endfunction


