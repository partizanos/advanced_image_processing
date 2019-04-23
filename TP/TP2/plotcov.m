function plotcov(mu,C,opt)
% FUNCTION PLOTCOV(MU,C) plots an ellipse associated with the covariance
% matrix stored in C at a position defined by the expectation vector MU.
% The plot is created as a red line in the current axis.
%
% Input:
% MU:   a 2-dimensional column vector denoting the mean vector of a
%       2-dimensional random vector
% COV:  the 2x2 covariance matrix associated with the random vector
% 
% The ellipse can be regarded as a region of uncertainty. For Gaussian
% variables about 40% of the data falls within this region.

if nargin==2, opt='r-'; end

[n,m] = size(mu);
if n~=2 && m~=1, error('mu must be a 2-dimensional column vector'); end;
[n,m] = size(C);
if n~=2 && m~=2, error('C must be a 2x2 matrix'); end; 
    

[E,L] = eig(C);                     % eigenvectors and eigenvalues of C

w=0:2*pi/99:2*pi;              % equidistant angles
nPoints=length(w);                  % nr of angles
rCircle=1*[cos(w);sin(w)];          % points on a unit circle
A=E*L^0.5;                          % define linear operator
rPlot=A*rCircle+mu*ones(1,nPoints); % transform the circle and shift it
plot(rPlot(1,:),rPlot(2,:),opt,'LineWidth',1');

% or:
% circle=rsmak('circle');
% fnplt(fncmb(fncmb(circle,E*sqrt(L)),mu),opt);
