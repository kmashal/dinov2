from dinov2.models.vision_transformer import vit_base

modle =vit_base()

for name, param in modle.named_parameters:
    print(name, param.shape)