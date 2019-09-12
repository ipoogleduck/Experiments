%% Import data from text file.
% Script for importing data from PACO-LOCO Task
% Date: 08.13.19
% Authors: Stefania + Oliver

% Subjects you want to analyze
ssids = [006, 008, 012, 014, 015];

% For each subject, load their file and compute variables of interest
for s = 1:length(ssids)
    subj = sprintf('%03d', ssids(s)); % convert to character with leading zeros (since matlab drops the leading zeros and we need them for the file name)
    
    %% IMPORT Subject Files
    % Initialize variables
    filename = sprintf('/Volumes/bamlab/Experiments/PACO/CO/data/%s/sub_%s_PACOCO_test.csv', subj, subj);
    delimiter = ',';
    startRow = 2;
    
    
    %%%%%%%%%%%%%%%%%%%%%%%%% DO NOT EDIT: Can be regenerated if files to be loaded change %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    %% Read columns of data as text:
    % For more information, see the TEXTSCAN documentation.
    formatSpec = '%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%q%[^\n\r]';
    
    %% Open the text file.
    fileID = fopen(filename,'r','n','UTF-8');
    % Skip the BOM (Byte Order Mark).
    fseek(fileID, 3, 'bof');
    
    %% Read columns of data according to the format.
    % This call is based on the structure of the file used to generate this
    % code. If an error occurs for a different file, try regenerating the code
    % from the Import Tool.
    dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter, 'TextType', 'string', 'HeaderLines' ,startRow-1, 'ReturnOnError', false, 'EndOfLine', '\r\n');
    
    %% Close the text file.
    fclose(fileID);
    
    %% Convert the contents of columns containing numeric text to numbers.
    % Replace non-numeric text with NaN.
    raw = repmat({''},length(dataArray{1}),length(dataArray)-1);
    for col=1:length(dataArray)-1
        raw(1:length(dataArray{col}),col) = mat2cell(dataArray{col}, ones(length(dataArray{col}), 1));
    end
    numericData = NaN(size(dataArray{1},1),size(dataArray,2));
    
    for col=[1,2,3,4,6,7,10,11,13,14,15,19,20,21,22,26]
        % Converts text in the input cell array to numbers. Replaced non-numeric
        % text with NaN.
        rawData = dataArray{col};
        for row=1:size(rawData, 1)
            % Create a regular expression to detect and remove non-numeric prefixes and
            % suffixes.
            regexstr = '(?<prefix>.*?)(?<numbers>([-]*(\d+[\,]*)+[\.]{0,1}\d*[eEdD]{0,1}[-+]*\d*[i]{0,1})|([-]*(\d+[\,]*)*[\.]{1,1}\d+[eEdD]{0,1}[-+]*\d*[i]{0,1}))(?<suffix>.*)';
            try
                result = regexp(rawData(row), regexstr, 'names');
                numbers = result.numbers;
                
                % Detected commas in non-thousand locations.
                invalidThousandsSeparator = false;
                if numbers.contains(',')
                    thousandsRegExp = '^\d+?(\,\d{3})*\.{0,1}\d*$';
                    if isempty(regexp(numbers, thousandsRegExp, 'once'))
                        numbers = NaN;
                        invalidThousandsSeparator = true;
                    end
                end
                % Convert numeric text to numbers.
                if ~invalidThousandsSeparator
                    numbers = textscan(char(strrep(numbers, ',', '')), '%f');
                    numericData(row, col) = numbers{1};
                    raw{row, col} = numbers{1};
                end
            catch
                raw{row, col} = rawData{row};
            end
        end
    end
    
    
    %% Split data into numeric and string columns.
    rawNumericColumns = raw(:, [1,2,3,4,6,7,10,11,13,14,15,19,20,21,22,26]);
    rawStringColumns = string(raw(:, [5,8,9,12,16,17,18,23,24,25]));
    
    
    %% Replace non-numeric cells with NaN
    R = cellfun(@(x) ~isnumeric(x) && ~islogical(x),rawNumericColumns); % Find non-numeric cells
    rawNumericColumns(R) = {NaN}; % Replace non-numeric cells
    
    %% Make sure any text containing <undefined> is properly converted to an <undefined> categorical
    for catIdx = [1,2,3,4,5,7,8,9,10]
        idx = (rawStringColumns(:, catIdx) == "<undefined>");
        rawStringColumns(idx, catIdx) = "";
    end
    
    %% Allocate imported array to column variable names
    StimuliName = cell2mat(rawNumericColumns(:, 1));
    TestOrder = cell2mat(rawNumericColumns(:, 2));
    OldOrNewOrder = cell2mat(rawNumericColumns(:, 3));
    StudyOrder = cell2mat(rawNumericColumns(:, 4));
    User_OldOrNew = categorical(rawStringColumns(:, 1));
    User_Color = cell2mat(rawNumericColumns(:, 5));
    User_Rad = cell2mat(rawNumericColumns(:, 6));
    User_AproxColor = categorical(rawStringColumns(:, 2));
    Correct_OldOrNew = categorical(rawStringColumns(:, 3));
    Correct_Color = cell2mat(rawNumericColumns(:, 7));
    Correct_Rad = cell2mat(rawNumericColumns(:, 8));
    Correct_AproxColor = categorical(rawStringColumns(:, 4));
    radColorDist = cell2mat(rawNumericColumns(:, 9));
    OldOrNew_RT = cell2mat(rawNumericColumns(:, 10));
    Test_RT1 = cell2mat(rawNumericColumns(:, 11));
    StudyStartTime = categorical(rawStringColumns(:, 5));
    OldOrNewStartTime = rawStringColumns(:, 6);
    TestStartTime = categorical(rawStringColumns(:, 7));
    StudyOnset = cell2mat(rawNumericColumns(:, 12));
    OldOrNewOnset = cell2mat(rawNumericColumns(:, 13));
    TestOnset = cell2mat(rawNumericColumns(:, 14));
    participant = cell2mat(rawNumericColumns(:, 15));
    date = categorical(rawStringColumns(:, 8));
    expName = categorical(rawStringColumns(:, 9));
    psychopyVersion = categorical(rawStringColumns(:, 10));
    frameRate = cell2mat(rawNumericColumns(:, 16));
    
    
    %% Clear temporary variables
    clearvars filename delimiter startRow formatSpec fileID dataArray ans raw col numericData rawData row regexstr result numbers invalidThousandsSeparator thousandsRegExp rawNumericColumns rawStringColumns R catIdx idx;
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    %% Recognition Performance (OldOrNew)
    isold = Correct_OldOrNew == 'Old'; %1 is old
    iscorrect = Correct_OldOrNew == User_OldOrNew;
    
    % Overall Accuracy
    recAcc(s,1) = nanmean(iscorrect);
    
    % Accuracy for old items (hit rate)
    recHR(s,1) = nanmean((User_OldOrNew(isold == 1) == 'Old'));
    
    % false alarm rate = saying something is old when it's actually new
    recFA(s,1) = nanmean((User_OldOrNew(isold == 0) == 'Old'));
    
    % Hit rate - false alarm rate (corrected hit rate)
    recCHR(s,1) = recHR(s,1) - recFA(s,1);
    
    % Average reaction time for correct old
    recORT(s,1) = nanmean((OldOrNew_RT(User_OldOrNew(isold == 1) == 'Old')));
    
    % Average reaction time for correct new
    recNRT(s,1) = nanmean((OldOrNew_RT(User_OldOrNew(isold == 0) == 'New')));
    
    
    %% Color Performance
    
    % Mean Average distance from correct color (overall)
    colorDistAll(s,1) = nanmean(radColorDist);
    
    % Median Average distance from correct color (overall)
    colorDistAllMed(s,1) = median(radColorDist,'omitnan');
    
    % Mean Average distance from correct color (when recognition was correct)
    colorDistCorrect(s,1) = nanmean(radColorDist(User_OldOrNew(isold == 1) == 'Old'));
    
    % Median Average distance from correct color (when recognition was correct)
    colorDistCorrectMed(s,1) = median(radColorDist(User_OldOrNew(isold == 1) == 'Old'),'omitnan');
    
end

%% Specify Output Data
% Assign File Headers by Task Stage
recognition_headers = {'OverallAcc', 'HR', 'FA', 'CHR', 'O_RT', 'N_RT', 'Mean_CDA', 'Mean_CDC', 'Median_CDA', 'Median_CDC'};
color_headers = {};
location_headers = {};

% Specify Output Variables by Task Stage
recognition_data = [recAcc, recHR, recFA, recCHR, recORT, recNRT];
color_data = [colorDistAll, colorDistCorrect, colorDistAllMed, colorDistCorrectMed];

% Compile Final Headers and total output data matrix
headers = [{'subjNumber'}, recognition_headers];
out_data = [ssids', recognition_data, color_data];


%% Create Analysis Directory
subDir = sprintf('%s/analysis', pwd);

if ~exist (subDir, 'dir')
    mkdir(subDir);
else
    warning('WARNING: This analysis directory already exists!');
    yn = input('Should I continue? (y,n): ', 's');
    o = yn(1);
    clear yn;
    if(~isequal(upper(o), 'Y'))
        sprintf('CANCELLED. Check subject number to see if there is existing data.')
        return
    end
end

%% Create Compiled Behave Data TXT File & .MAT
compiledBehave = sprintf('%s/Analysis/co_compiledBehave.txt', pwd);

% Open the file and flag if new or appending additional subjects
% to existing file.
fid = fopen(compiledBehave, 'w');

for h = 1:length(headers)
    fprintf(fid, [headers{h} '\t']);
end

fprintf(fid, '\n');
fclose(fid);

% Write text file
dlmwrite(compiledBehave,out_data,'delimiter','\t','precision',4,'-append');
% Wrtie .mat file
save(sprintf('%s/co_compiledBehave.mat',subDir), 'out_data');

% Clear the Workspace
clear all
