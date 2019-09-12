function [struct] = buildTrialStructure(cond,p)

s = fieldnames(cond);
struct = [];
reps = 1;
for i=1:length(s)
    curVal = getfield(cond,s{i});
    c = [];

    if iswhole(p.nTrials/(curVal*reps)) == 0
        Screen('CloseAll');
        msgbox(['Invalid Trial Number'], 'modal')
        return;
    end

    for r = 1:reps
        for t = 1:curVal
            c = [c, repmat(t,1,p.nTrials/(curVal*reps))];
        end
    end
    struct = [struct; c];
    reps = reps*curVal;
end