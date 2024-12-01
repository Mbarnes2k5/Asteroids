-- Function to set terminal title
local function set_terminal_title(title)
	io.write("\27]0;" .. title .. "\7")
end

set_terminal_title("My Terminal Title")
