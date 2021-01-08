function T890822ASC = fun_import(filename, dataLines)

if nargin < 2
    dataLines = [1, Inf];
end

opts = delimitedTextImportOptions("NumVariables", 16);

opts.DataLines = dataLines;
opts.Delimiter = ",";

opts.VariableNames = ["T000047663Z", "VarName2", "VarName3", "VarName4", "VarName5", "VarName6", "VarName7", "VarName8", "VarName9", "VarName10", "VarName11", "VarName12", "VarName13", "VarName14", "VarName15", "VarName16"];
opts.VariableTypes = ["double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double", "double"];

opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";

opts = setvaropts(opts, "T000047663Z", "TrimNonNumeric", true);
opts = setvaropts(opts, "T000047663Z", "ThousandsSeparator", ",");

T890822ASC = readtable(filename, opts);

T890822ASC = table2array(T890822ASC);
end