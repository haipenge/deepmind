    @GenerateEntityProperty
    /**
	 * @说明:${obj.title}<br>
	 * @属性名: ${obj.get_property_name()}<br>
	 * @类型: ${obj.type}<br>
	 * @数据库字段:${obj.get_column_name()}<br>
	 * @author haipenge<br>
	 */
	@Column(name="${obj.get_column_name()}")
	private ${obj.type} ${obj.get_property_name()}=${obj.get_default_value()};
	public ${obj.type} get${obj.get_method_name()}() {
		return ${obj.get_property_name()};
	}

	public void set${obj.get_method_name()}(${obj.type} ${obj.get_property_name()}) {
		this.${obj.get_property_name()} = ${obj.get_property_name()};
	}