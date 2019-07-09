# I define the blocks!

def blockcheck(blockname, blockwanted, blockget):
    if blockname == blockwanted:
        return(blockget)

def get_block(bn):
    import mcpi.block as block
    gotblock = block.AIR
    # wood
    gotblock = blockcheck(bn, "log_acacida.png", block.ACACIA_WOOD)
    gotblock = blockcheck(bn, "planks_acacia.png", block.WOOD_PLANKS_ACACIA)
    gotblock = blockcheck(bn, "log_big_oak.png", block.DARK_OAK_WOOD)
    gotblock = blockcheck(bn, "planks_big_oak.png", block.WOOD_PLANKS_DARK_OAK)
    gotblock = blockcheck(bn, "log_oak.png", block.WOOD)
    gotblock = blockcheck(bn, "planks_oak.png", block.WOOD_PLANKS_OAK)
    gotblock = blockcheck(bn, "log_birch.png", block.BIRCH_WOOD)
    gotblock = blockcheck(bn, "planks_birch.png", block.WOOD_PLANKS_BIRCH)
    gotblock = blockcheck(bn, "log_spruce.png", block.SPRUCE_WOOD)
    gotblock = blockcheck(bn, "planks_spruce.png", block.WOOD_PLANKS_SPRUCE)
    gotblock = blockcheck(bn, "log_jungle.png", block.JUNGLE_WOOD)
    gotblock = blockcheck(bn, "planks_jungle.png", block.WOOD_PLANKS_JUNGLE)
    # wool
    gotblock = blockcheck(bn, "wool_colored_black.png", block.WOOL_BLACK)
    gotblock = blockcheck(bn, "wool_colored_blue.png", block.WOOL_BLUE)
    gotblock = blockcheck(bn, "wool_colored_brown.png", block.WOOL_BROWN)
    gotblock = blockcheck(bn, "wool_colored_cyan.png", block.WOOL_CYAN)
    gotblock = blockcheck(bn, "wool_colored_gray.png", block.WOOL_GRAY)
    gotblock = blockcheck(bn, "wool_colored_green.png", block.WOOL_GREEN)
    gotblock = blockcheck(bn, "wool_colored_light_blue.png", block.WOOL_LIGHT_BLUE)
    gotblock = blockcheck(bn, "wool_colored_lime.png", block.WOOL_LIME)
    gotblock = blockcheck(bn, "wool_colored_magenta.png", block.WOOL_MAGENTA)
    gotblock = blockcheck(bn, "wool_colored_orange.png", block.WOOL_ORANGE)
    gotblock = blockcheck(bn, "wool_colored_pink.png", block.WOOL_PINK)
    gotblock = blockcheck(bn, "wool_colored_purple.png", block.WOOL_PURPLE)
    gotblock = blockcheck(bn, "wool_colored_red.png", block.WOOL_RED)
    gotblock = blockcheck(bn, "wool_colored_silver.png", block.WOOL_LIGHT_GRAY)
    gotblock = blockcheck(bn, "wool_colored_white.png", block.WOOL_WHITE)
    gotblock = blockcheck(bn, "wool_colored_yellow.png", block.WOOL_YELLOW)
    # concrete
    gotblock = blockcheck(bn, "concrete_black.png", block.CONCRETE_BLOCK_BLACK)
    gotblock = blockcheck(bn, "concrete_blue.png", block.CONCRETE_BLOCK_BLUE)
    gotblock = blockcheck(bn, "concrete_brown.png", block.CONCRETE_BLOCK_BROWN)
    gotblock = blockcheck(bn, "concrete_cyan.png", block.CONCRETE_BLOCK_CYAN)
    gotblock = blockcheck(bn, "concrete_gray.png", block.CONCRETE_BLOCK_GRAY)
    gotblock = blockcheck(bn, "concrete_green.png", block.CONCRETE_BLOCK_GREEN)
    gotblock = blockcheck(bn, "concrete_light_blue.png", block.CONCRETE_BLOCK_LIGHT_BLUE)
    gotblock = blockcheck(bn, "concrete_lime.png", block.CONCRETE_BLOCK_LIME)
    gotblock = blockcheck(bn, "concrete_magenta.png", block.CONCRETE_BLOCK_MAGENTA)
    gotblock = blockcheck(bn, "concrete_orange.png", block.CONCRETE_BLOCK_ORANGE)
    gotblock = blockcheck(bn, "concrete_pink.png", block.CONCRETE_BLOCK_PINK)
    gotblock = blockcheck(bn, "concrete_purple.png", block.CONCRETE_BLOCK_PURPLE)
    gotblock = blockcheck(bn, "concrete_red.png", block.CONCRETE_BLOCK_RED)
    gotblock = blockcheck(bn, "concrete_silver.png", block.CONCRETE_BLOCK_LIGHT_GRAY)
    gotblock = blockcheck(bn, "concrete_white.png", block.CONCRETE_BLOCK_WHITE)
    gotblock = blockcheck(bn, "concrete_yellow.png", block.CONCRETE_BLOCK_YELLOW)
    # other blocks
    gotblock = blockcheck(bn, "brick.png", block.BRICK_BLOCK)
    gotblock = blockcheck(bn, "diamond_block.png", block.DIAMOND_BLOCK)
    gotblock = blockcheck(bn, "emerand_block.png", block.EMERALD_BLOCK)
    gotblock = blockcheck(bn, "gold_block.png", block.GOLD_BLOCK)
    gotblock = blockcheck(bn, "iron_block.png", block.IRON_BLOCK)
    gotblock = blockcheck(bn, "lapis_block.png", block.LAPIS_LAZULI_BLOCK)
    gotblock = blockcheck(bn, "purpur_block.png", block.REDSTONE_BLOCK)
    gotblock = blockcheck(bn, "redstone_block.png", block.PURPUR_BLOCK)
    # give info
    return(gotblock)
