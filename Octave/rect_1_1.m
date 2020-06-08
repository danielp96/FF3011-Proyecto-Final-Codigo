
function rect_1_1()

    graphics_toolkit('gnuplot');

    mkdir('rect_1.1');

    graph_n('rect_1.1/figure_n_2',   2);
    graph_n('rect_1.1/figure_n_5',   5);
    graph_n('rect_1.1/figure_n_10',   10);
    graph_n('rect_1.1/figure_n_20',   20);

endfunction

function v = volt(x,y,a,b,n, const)

    v=const*sinh(n*pi*x/b)*sin(n*pi*y/b);

endfunction

function e = e_field(x,y,a,b,n, const)

    ex = cosh(n*pi*x/b)*sin(n*pi*y/b);

    ey = sinh(n*pi*x/b)*cos(n*pi*y/b);

    e=const*(n*pi/b)*sqrt(ex^2+ey^2);

endfunction

function s = charge(y,a,b,n, const)

    s = const*(n*pi/b)*cosh(n*pi*a/b)*sin(n*pi*y/b);

endfunction

function graph_v(name, n, a, b, const)

    V(a+1,b+1)=0;

    for ix=1:a+1
        for iy=1:b+1
            V(ix,iy)=volt(ix,iy,a,b,n, const);
        end
    end

    x=0:1:a;
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

    for ix=1:a+1
        for iy=1:b+1
            E(ix,iy)=e_field(ix,iy,a,b,n, const);
        end
    end

    x=0:1:a;
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


function graph_s(name, n, a, b, const)

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

    file_name = sprintf('%s_s', name);
    print('-dpng',file_name);

endfunction

function graph_n(name, n)
    a=200;
    b=100;

    % pre calculating magic constant ;)

    const=atan(b/a)*sin(n*pi);
    for i=1:4
        const = const + 2*atan(i*b/(a*10))*sin(n*pi*i/10);
    end

    const = const*0.1/sinh(n*pi*a/b);

    graph_v(name,   n, a, b, const);
    graph_e(name,   n, a, b, const);
    graph_s(name,   n, a, b, const);

endfunction



