import bpy

def create_hello_world_shader(tile_path):
    # Create a new material
    mat = bpy.data.materials.new(name="HelloWorldShader")
    mat.use_nodes = True  # Enable nodes

    # Clear default nodes
    nodes = mat.node_tree.nodes
    for node in nodes:
        nodes.remove(node)

    # Add new nodes
    output_node = nodes.new(type="ShaderNodeOutputMaterial")
    output_node.location = (400, 0)

    emission_node = nodes.new(type="ShaderNodeEmission")
    emission_node.location = (200, 0)

    text_node = nodes.new(type="ShaderNodeTexImage")
    text_node.location = (0, 0)

    # Load the bricks.png image as the texture
    img = bpy.data.images.load(tile_path)

    # Assign image to the text node
    text_node.image = img

    # Link nodes
    links = mat.node_tree.links
    links.new(text_node.outputs['Color'], emission_node.inputs['Color'])
    links.new(emission_node.outputs['Emission'], output_node.inputs['Surface'])

    return mat

# Path to the bricks.png tile (ensure this path is correct)
tile_path = "brick.png"  # Replace with the actual path to bricks.png

# Create the shader and assign it to the active object
if bpy.context.object:
    obj = bpy.context.object
    mat = create_hello_world_shader(tile_path)

    if len(obj.data.materials) == 0:
        obj.data.materials.append(mat)
    else:
        obj.data.materials[0] = mat

print("Hello World Shader with bricks.png applied!")
