# I define the blocks!
import mcpi.block as block

glock = ""

def blockcheck(blockname, blockwanted, blockget):
    global glock
    if str(blockname) == str(blockwanted):
        glock = blockget

def get_block(bn):
    global glock
    # wood
    blockcheck(bn, "log_acacida.png", block.ACACIA_WOOD)
    blockcheck(bn, "planks_acacia.png", block.WOOD_PLANKS_ACACIA)
    blockcheck(bn, "log_big_oak.png", block.DARK_OAK_WOOD)
    blockcheck(bn, "planks_big_oak.png", block.WOOD_PLANKS_DARK_OAK)
    blockcheck(bn, "log_oak.png", block.WOOD)
    blockcheck(bn, "planks_oak.png", block.WOOD_PLANKS_OAK)
    blockcheck(bn, "log_birch.png", block.BIRCH_WOOD)
    blockcheck(bn, "planks_birch.png", block.WOOD_PLANKS_BIRCH)
    blockcheck(bn, "log_spruce.png", block.SPRUCE_WOOD)
    blockcheck(bn, "planks_spruce.png", block.WOOD_PLANKS_SPRUCE)
    blockcheck(bn, "log_jungle.png", block.JUNGLE_WOOD)
    blockcheck(bn, "planks_jungle.png", block.WOOD_PLANKS_JUNGLE)
    # wool
    blockcheck(bn, "wool_colored_black.png", block.WOOL_BLACK)
    blockcheck(bn, "wool_colored_blue.png", block.WOOL_BLUE)
    blockcheck(bn, "wool_colored_brown.png", block.WOOL_BROWN)
    blockcheck(bn, "wool_colored_cyan.png", block.WOOL_CYAN)
    blockcheck(bn, "wool_colored_gray.png", block.WOOL_GRAY)
    blockcheck(bn, "wool_colored_green.png", block.WOOL_GREEN)
    blockcheck(bn, "wool_colored_light_blue.png", block.WOOL_LIGHT_BLUE)
    blockcheck(bn, "wool_colored_lime.png", block.WOOL_LIME)
    blockcheck(bn, "wool_colored_magenta.png", block.WOOL_MAGENTA)
    blockcheck(bn, "wool_colored_orange.png", block.WOOL_ORANGE)
    blockcheck(bn, "wool_colored_pink.png", block.WOOL_PINK)
    blockcheck(bn, "wool_colored_purple.png", block.WOOL_PURPLE)
    blockcheck(bn, "wool_colored_red.png", block.WOOL_RED)
    blockcheck(bn, "wool_colored_silver.png", block.WOOL_LIGHT_GRAY)
    blockcheck(bn, "wool_colored_white.png", block.WOOL_WHITE)
    blockcheck(bn, "wool_colored_yellow.png", block.WOOL_YELLOW)
    # concrete
    blockcheck(bn, "concrete_black.png", block.CONCRETE_BLOCK_BLACK)
    blockcheck(bn, "concrete_blue.png", block.CONCRETE_BLOCK_BLUE)
    blockcheck(bn, "concrete_brown.png", block.CONCRETE_BLOCK_BROWN)
    blockcheck(bn, "concrete_cyan.png", block.CONCRETE_BLOCK_CYAN)
    blockcheck(bn, "concrete_gray.png", block.CONCRETE_BLOCK_GRAY)
    blockcheck(bn, "concrete_green.png", block.CONCRETE_BLOCK_GREEN)
    blockcheck(bn, "concrete_light_blue.png", block.CONCRETE_BLOCK_LIGHT_BLUE)
    blockcheck(bn, "concrete_lime.png", block.CONCRETE_BLOCK_LIME)
    blockcheck(bn, "concrete_magenta.png", block.CONCRETE_BLOCK_MAGENTA)
    blockcheck(bn, "concrete_orange.png", block.CONCRETE_BLOCK_ORANGE)
    blockcheck(bn, "concrete_pink.png", block.CONCRETE_BLOCK_PINK)
    blockcheck(bn, "concrete_purple.png", block.CONCRETE_BLOCK_PURPLE)
    blockcheck(bn, "concrete_red.png", block.CONCRETE_BLOCK_RED)
    blockcheck(bn, "concrete_silver.png", block.CONCRETE_BLOCK_LIGHT_GRAY)
    blockcheck(bn, "concrete_white.png", block.CONCRETE_BLOCK_WHITE)
    blockcheck(bn, "concrete_yellow.png", block.CONCRETE_BLOCK_YELLOW)
    # other blocks
    blockcheck(bn, "brick.png", block.BRICK_BLOCK)
    blockcheck(bn, "diamond_block.png", block.DIAMOND_BLOCK)
    blockcheck(bn, "emerand_block.png", block.EMERALD_BLOCK)
    blockcheck(bn, "gold_block.png", block.GOLD_BLOCK)
    blockcheck(bn, "iron_block.png", block.IRON_BLOCK)
    blockcheck(bn, "lapis_block.png", block.LAPIS_LAZULI_BLOCK)
    blockcheck(bn, "purpur_block.png", block.PURPUR_BLOCK)
    blockcheck(bn, "redstone_block.png", block.REDSTONE_BLOCK)

    blockcheck(bn, "bedrock.png", block.BEDROCK)
    blockcheck(bn, "end_bricks.png", block.END_BRICKS)
    blockcheck(bn, "obsidian.png", block.OBSIDIAN)
    blockcheck(bn, "prismarine_bricks.png", block.PRISMARINE_BRICKS)
    blockcheck(bn, "red_nether_brick.png", block.RED_NETHER_BRICK)
    blockcheck(bn, "stonebrick_carved.png", block.STONE_BRICK_CHISELED)
    blockcheck(bn, "stonebrick_cracked.png", block.STONE_BRICK_CRACKED)
    blockcheck(bn, "stonebrick_mossy.png", block.STONE_BRICK_MOSSY)
    blockcheck(bn, "stonebrick.png", block.STONE_BRICK)
    blockcheck(bn, "nether_brick.png", block.NETHER_BRICK)
    blockcheck(bn, "bookshelf.png", block.BOOKSHELF)
    # give info
    return(glock)
