from fastai.vision.all import *
            
def sum_splitter(sum_model): return [params(sum_model.models[0][0]), 
                                     params(sum_model.models[1][0]), 
                                     params(sum_model.models[2][0]), 
                                     params(sum_model.models[3][0]), 
                                     params(sum_model.models[4][0]), 
                                     params(sum_model.models[5][0]), 
                                     params(sum_model.models[6][0]), 
                                     params(sum_model.models[7][0]), 
                                     params(sum_model.models[8][0]), 
                                     params(sum_model.models[9][0]), 
                                     params(sum_model.models[10][0]), 
                                     params(sum_model.models[11][0]), 
                                     params(sum_model.models[12][0]), 
                                     params(sum_model.models[13][0]), 
                                     params(sum_model.models[14][0]), 
                                     params(sum_model.models[0][1]), 
                                     params(sum_model.models[1][1]), 
                                     params(sum_model.models[2][1]), 
                                     params(sum_model.models[3][1]), 
                                     params(sum_model.models[4][1]), 
                                     params(sum_model.models[5][1]), 
                                     params(sum_model.models[6][1]), 
                                     params(sum_model.models[7][1]), 
                                     params(sum_model.models[8][1]), 
                                     params(sum_model.models[9][1]), 
                                     params(sum_model.models[10][1]), 
                                     params(sum_model.models[11][1]), 
                                     params(sum_model.models[12][1]), 
                                     params(sum_model.models[13][1]), 
                                     params(sum_model.models[14][1]),
                                     params(sum_model.models[15].embeds),
                                     params(sum_model.mixed_cls)] 