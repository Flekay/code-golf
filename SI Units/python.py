import sys
P=dict(zip('QRYZEPTGMkh~dcmμnpfazyrq',[*range(30,2,-3),2,1,-1,-2,*range(-3,-31,-3)]))
U=dict(zip("cd s g A m K mol rad sr Hz N Pa J W C V F Ω S Wb T H °C lm lx Bq Gy Sv kat".split(),"cd_s_kg_A_m_K_mol___s^-1_kg m s^-2_kg m^-1 s^-2_kg m^2 s^-2_kg m^2 s^-3_A s_kg m^2 s^-3 A^-1_kg^-1 m^-2 s^4 A^2_kg m^2 s^-3 A^-2_kg^-1 m^-2 s^3 A^2_kg m^2 s^-2 A^-1_kg s^-2 A^-1_kg m^2 s^-2 A^-2_K_cd_cd m^-2_s^-1_m^2 s^-2_m^2 s^-2_mol s^-1".split("_")))
for a in sys.argv[1:]:B=(a:=a.replace("da","~"))in U;print({0:1,1:10}.get(C:=(B-1and P[a[0]])-3*('g'in a),f"10^{C}"),U[a[1-B:]])
